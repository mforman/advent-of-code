#load "common.fsx"
open Common

let parseItem (item:string) =
    item.Split('x') |> Array.map(int)

let areaWithPad dimensions = 
    let sides = 
        dimensions 
        |> Array.permute (fun i -> (i+1) % 3) 
        |> Array.zip dimensions 
        |> Array.map (fun (x,y) -> x*y)
        
    let smallest = sides |> Array.sort |> Array.head

    sides |> Array.fold (fun acc elem -> acc + (2 * elem)) smallest

let ribbonLength dimensions =
    let volume = dimensions |> Array.reduce (*)
    dimensions
    |> Array.sort
    |> Array.take 2
    |> Array.map (fun x -> x * 2)
    |> Array.fold (+) volume


let solve fn input =
    let items = input |> Array.map parseItem
    items |> Array.map fn |> Array.reduce (+)
    
let solvePart1 = solve areaWithPad
let solvePart2 = solve ribbonLength