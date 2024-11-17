#load @"Day10.fsx"
open System
open Day10

// let generateInput (key:string) =
//     [| 0..127 |]
//     |> Seq.map (sprintf "%s-%d" key)
// let charToBin c = 
//     let s = sprintf "0x%c" c
//     let i = Convert.ToInt32(s, 16)
//     [ ((i &&& 8)/8); ((i &&& 4)/4); ((i &&& 2)/2); (i &&& 1); ]


// let stringToBin s =
//     s |> Seq.collect charToBin

// let stringToBinStr s =
//     s |> Seq.collect charToBinStr

// let getActiveColumns key =
//     generateInput key
//     |> Seq.map Day10.solvePart2
//     |> Seq.map stringToBinStr
//     |> Seq.mapi (fun i c -> (i, c))


// let solvePart1 key =
//     generateInput key
//     |> Seq.map Day10.solvePart2
//     |> Seq.collect stringToBin
//     |> Seq.sum


let charToBinStr c = 
    let s = sprintf "0x%c" c
    let i = Convert.ToInt32(s, 16)
    Convert.ToString(i, 2).PadLeft(4, '0')
let getHash key i = 
    Day10.solvePart2 (sprintf "%s-%d" key i) 
    |> Seq.collect charToBinStr

let hashToCoords i = Seq.mapi (fun j h -> ((i, j), h)) >> Seq.filter (snd >> ((=) '1')) >> Seq.map fst >> Set.ofSeq
let getActiveCoords key =
    Seq.map (getHash key) [0..127]
    |> Seq.mapi hashToCoords
    |> Set.unionMany

let solvePart1 key = getActiveCoords key |> Set.count

let rec getComponentCount seen unseen count = function
    | [] when Set.isEmpty unseen -> count
    | [] -> getComponentCount seen unseen (count + 1) [Seq.head unseen]
    | x :: xs when Set.contains x seen || not (Set.contains x unseen) -> getComponentCount seen unseen count xs
    | (i, j) :: xs -> getComponentCount (Set.add (i, j) seen) (Set.remove (i, j) unseen) count ((i-1,j)::(i+1,j)::(i,j-1)::(i,j+1)::xs)


let solvePart2 key = getComponentCount Set.empty (getActiveCoords key) 0 []



