#load "common.fsx"
open Common
open System

type Point = {x:float; y:float}
    with member this.StepsAway = Math.Abs(this.x) + Math.Abs(this.y)
    with static member Zero = {x=0.0; y=0.0;}

let step start direction =
    match direction with
    | "n" -> { start with y = start.y + 1.0 }
    | "s" -> { start with y = start.y - 1.0 }
    | "ne" -> { start with x = start.x + 0.5; y = start.y + 0.5 }
    | "se" -> { start with x = start.x + 0.5; y = start.y - 0.5 }
    | "nw" -> { start with x = start.x - 0.5; y = start.y + 0.5 }
    | "sw" -> { start with x = start.x - 0.5; y = start.y - 0.5 }
    | _ -> start

let parseAndProcess (processor:string[] -> Point) (input:string) =
    let moves = input.Split(',')
    let finsih = processor moves
    finsih.StepsAway |> int

let solvePart1 = parseAndProcess (fun x -> x |> Array.fold step Zero)
let solvePart2 = parseAndProcess (fun x -> x |> Array.scan step Zero |> Array.maxBy (fun p -> p.StepsAway))