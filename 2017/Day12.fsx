#load "common.fsx"
open Common

let parseInput (lines:string []) =
    lines
    |> Array.map (
        function
        | Regex @"(\d+) <-> (.*)" [x; y] ->
            int x,
            y.Split(',') |> Array.map (fun e -> e.Trim() |> int)
        | _ -> failwith "Invalid input"
    )
    |> Map.ofArray

let solve (lines:string []) =
    let mapping = parseInput lines

    let rec find seen root =
        if Set.contains root seen then
            seen
        else
            Array.fold find (seen.Add root) mapping.[root]
    
    let part1 = find Set.empty 0 |> Set.count

    let countComponents (count, seen) (num, _) =
        if Set.contains num seen then
            (count, seen)
        else 
            (count + 1, find seen num)

    let part2 = 
        mapping 
        |> Map.toSeq
        |> Seq.fold countComponents (0, Set.empty)
        |> fst

    (part1, part2)

let raw = readLines "12-input.txt"
solve raw