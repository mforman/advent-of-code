#load "common.fsx"
open Common
let parseInput (lines:string []) =
    lines
    |> Array.map (
        function
        | Regex @"(\d+): (\d+)" [x; y] ->
            int x,
            2 * (int y - 1),
            int y
        | _ -> failwith "Invalid input"
    )

let severity (depth, sweep, range) = 
    if (depth % sweep) = 0 then depth * range
    else 0

let notCaughtAt x (depth, sweep, _) =(x + depth) % sweep <> 0

let solvePart1 fileName = 
    readLines fileName
    |> parseInput
    |> Array.sumBy severity

let solvePart2 fileName =
    let input = 
        readLines fileName
        |> parseInput
    
    let rec findZero x = 
        match input |> Array.forall (notCaughtAt x) with
        | true -> x
        | false -> findZero (x+1)
    findZero 0

