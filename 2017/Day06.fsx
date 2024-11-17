#load "common.fsx"
open Common
let clone (array: int[]) = array.Clone () :?> int array

type Result = { Total: int; Loop: int; }

let rec cycle banks previous =
    let index, amount = banks |> Array.mapi (fun i v -> i,v) |> Array.maxBy snd
    banks.[index] <- 0
    for i = 1 to amount do
        let next = (index + i) % banks.Length
        banks.[next] <- banks.[next] + 1
    
    if previous |> Map.containsKey banks then
        { Total = previous.Count + 1; Loop = previous.Count - previous.[banks] }
    else
        previous
        |> Map.add (clone banks) previous.Count
        |> cycle banks

let solve input =
    let banks = parseList int input
    cycle banks Map.empty


// let realloc b =
//     let len = b |> List.length
//     let array = b |> List.toArray
//     let mutable x,y = b |> List.sortByDescending (fun (x, y) -> y + (1-(x/10))) |> List.head
//     array.[x] <- (x, 0)
//     x <- if x+1 = len then 0 else x+1
//     while y > 0 do
//         let _, current = array.[x]
//         array.[x] <- (x, current + 1)
//         y <- y - 1
//         x <- if x+1 = len then 0 else x+1
//     array |> Array.toList

// let rec solvePart1 banks =
//     let current = banks |> List.head
//     let next = current |> realloc
//     if banks |> List.exists (fun x -> x = next) then 
//         banks |> List.length
//     else
//         solvePart1 (banks |> List.append [current])

