let folder floor direction =
    match direction with
    | '(' -> floor + 1
    | ')' -> floor - 1
    | _ -> floor

let solvePart1 (input:string) = 
    input |> Seq.fold folder 0

let solvePart2 (input:string) =
    input |> Seq.scan folder 0 |> Seq.findIndex (fun x -> x = -1)