open System
open System.IO

type Point = { x: int; y: int; }
type Position = { location: Point; heading: int; history: Point list}
let turn pos dir = 
    match dir with
    | "R" -> { pos with heading = if pos.heading = 270 then 0 else pos.heading + 90 }
    | "L" -> { pos with heading = if pos.heading = 0 then 270 else pos.heading - 90 }
    | _ -> pos
 
let move pos steps =
    let deltaX, deltaY = 
        match pos.heading with
        | 0 -> (0, 1)
        | 90 -> (1, 0)
        | 180 -> (0, -1)
        | 270 -> (-1, 0)
        | _ -> (0, 0)
    let start = pos.location
    let hist = if List.isEmpty pos.history then [ start ] else pos.history
    let points = [0..steps] |> List.map (fun i -> { x = start.x + (i * deltaX); y = start.y + (i * deltaY); })
    { pos with location = points.[steps]; history = List.append hist points.[1..] }

let rec followMoves start moves =
    if List.isEmpty moves then
        start
    else
        let dir,steps = moves.[0]
        let turned = turn start dir
        let current = move turned steps
        followMoves current moves.[1..]

let rec haveWeBeenHere current prev rest =
    if List.contains current prev then
        Some(current)
    elif List.isEmpty rest then
        None
    else
        haveWeBeenHere rest.[0] (List.append prev [current]) rest.[1..]

let getDistanceBetweenPoints a b =
    (abs b.x - a.x) + (abs b.y - a.y)

let getDistance a b =
    getDistanceBetweenPoints a.location b.location

let moveParser str =
    if String.IsNullOrWhiteSpace(str) then
        ("", 0)
    else
        let clean = str.Trim()
        ((clean.[0]) |> string, (clean.[1..]) |> int)



// let instructions = "R8, R4, R4, R8"
let instructions = File.ReadAllText("./01/input.txt")

let moves = instructions.Split(',') |> Array.toList |> List.map moveParser

let start = { location = {x = 0; y = 0}; heading = 0; history = []}
let finish = followMoves start moves

getDistance start finish

let firstOverlap = haveWeBeenHere finish.history.[0] [] finish.history.[1..]

match firstOverlap with
| Some p -> getDistanceBetweenPoints start.location p
| None -> -1
