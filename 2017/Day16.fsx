#load "common.fsx"
open Common
open System

type Spin = 
    { size: int }
type Exchange = 
    { a: int; b:int }
type Partner = 
    { a: char; b: char }
type Move = Spin of Spin | Exchange of Exchange | Partner of Partner

let clone (array: char[]) = array.Clone () :?> char array
let Parse (instructions: string) =
    instructions.Split(',')
    |> Array.map (
        function
        | Regex @"(s|x|p)([a-z]|\d+)(?:/([a-z]|\d+))?" [m; a; b;] ->
            match m with
            | "s" -> Spin { size = int a; }
            | "x" -> Exchange { a = int a; b = int b; }
            | "p" -> Partner { a = char a; b = char b; }
            | _ -> failwith "Invalid Input"
        | _ -> failwith "Invalid Input"
    )

let ApplyMove (programs: char[]) (move: Move) =
    match move with
    | Spin s -> 
        let l = Array.length programs - 1
        let tail = programs.[l - s.size + 1..l]
        let head = programs.[0..l - s.size]
        Array.append tail head
    | Exchange x ->
        let p' = clone programs
        p'.[x.a] <- programs.[x.b]
        p'.[x.b] <- programs.[x.a]
        p'
    | Partner p ->
        let p' = clone programs
        let a = programs |> Array.findIndex (fun x -> x = p.a)
        let b = programs |> Array.findIndex (fun x -> x = p.b)
        p'.[a] <- programs.[b]
        p'.[b] <- programs.[a]
        p'
    | _ -> programs


let danceOnce state moves =
    moves |> Array.fold ApplyMove state

let rec danceMany state moves history =
    let x = danceOnce state moves
    if history |> List.contains x then
        let r = history |> List.rev
        let l = history |> List.length
        let m = 1000000000 % l
        r |> List.item m
    else
        danceMany x moves (x :: history)

let Programs = Array.init 16 (fun i -> char (97+i))
let input = readAll "16-input.txt"
let moves = Parse input

let solvePart1 = 
    let finalState = danceOnce Programs moves
    new string(finalState)

let solvePart2 = 
    let finalState = danceMany Programs moves [Programs]
    new string(finalState)
