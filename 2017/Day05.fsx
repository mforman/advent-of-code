let readLines filePath = System.IO.File.ReadLines(filePath)
let input = readLines "2017\\05\\sample.txt" |> Seq.map int

let AdvanceArray incrementer (items:int[]) (pos:int) =
    let steps = items.[pos]
    items.[pos] <- incrementer steps
    pos + steps

let rec Escape incrementer items  =
    let array = Seq.toArray items
    let mutable count = 0
    let mutable position = 0

    let len = array |> Array.length

    while position < len do
       position <- AdvanceArray incrementer array position
       count <- count + 1
    
    count
let EscapePart1 (items:int seq) = Escape (fun i -> i + 1) items
let EscapePart2 (items:int seq) = Escape (fun i -> i + if i >= 3 then -1 else 1) items
