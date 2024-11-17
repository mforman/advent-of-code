#load "common.fsx"
open Common

let clone (array: int[]) = array.Clone () :?> int array

type State = {Numbers: int[]; Pos:int; Skip:int}
    with member this.Hash = if this.Numbers.Length < 2 then 0 else this.Numbers.[0] * this.Numbers.[1]
let init len = { Numbers=Array.init len (id); Pos=0; Skip=0;}

let move len state =
    let numbers = state.Numbers |> clone
    let sub = 
        Array.init len (id) 
        |> Array.map (fun i -> state.Numbers.[(state.Pos + i) % state.Numbers.Length])
        |> Array.rev

    sub |> Array.mapi (fun i j -> numbers.[(state.Pos + i) % state.Numbers.Length] <- j) |> ignore

    { state with 
        Numbers = numbers; 
        Pos = (state.Pos + state.Skip + len) % state.Numbers.Length; 
        Skip = state.Skip + 1 }

let knotOnce state input =
    input |> Array.fold (fun acc elem -> move elem acc) state

let knotMultiple state input times =
    [|0..(times - 1)|] |> Array.fold (fun acc _ -> knotOnce acc input) state

let parseInputPart1 (s:string) = s.Split(',') |> Array.map (int)
let parseInputPart2 (s:string) = 
    let parsed = s |> Seq.map(fun c -> c |> int) 
    Seq.append parsed [17; 31; 73; 47; 23] |> Seq.toArray
let solvePart1 (input:string) =
    let parsed = parseInputPart1 input
    let initialState = init 256
    let finalState = parsed |> knotOnce initialState
    finalState.Hash

let solvePart2 (input:string) =
    let parsed = parseInputPart2 input
    let initialState = init 256
    let finalState = knotMultiple initialState parsed 64
    finalState.Numbers
    |> Array.chunkBySize 16
    |> Array.map (Array.reduce (^^^) >> sprintf "%02x")
    |> String.concat ""
    

