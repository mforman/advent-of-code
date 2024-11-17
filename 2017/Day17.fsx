(*
    0 [0]
    1 [0] -> [ 0 (1) ]
    2 [ 0 1 ] -> 

*)

type Move = {
    Position : int
    Items : int list
}

let spin numMoves value start =
    let pos = (numMoves + 1 - start.Position) % start.Items.Length
    let head,tail = start.Items |> List.splitAt pos
    let newItems = head @ [value] @ tail
    { Position = pos + 1; Items = newItems }

let moves = [ 1 .. 3 ]
let start = { Position = 0; Items = [0] }
let spinner = spin 3
let result = moves |> List.scan (fun acc elem -> spinner elem acc) start


