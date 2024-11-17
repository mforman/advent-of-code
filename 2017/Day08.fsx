#load "common.fsx"
open Common

open System.Collections.Generic


type Instruction = {
    register: string
    operation: int
    amount: int
    condition: string
    checkRegister: string
    checkValue: int
}

let getMultipler s =
    match s with
    | "inc" -> 1
    | "dec" -> -1
    | _ -> 0

let splitOnSpace (s:string) =
    s.Split(' ') |> Seq.toList

let parseLine line =
    let items = line |> splitOnSpace
    { 
        register = items.[0]; 
        operation = items.[1] |> getMultipler; 
        amount = items.[2] |> int; 
        condition = items.[4]; 
        checkRegister = items.[3]; 
        checkValue = items.[5] |> int 
    }

let parseInput lines = 
    lines |> Seq.map parseLine

let getRegisterValue (registers: Dictionary<string, int>) register =
    if registers.ContainsKey(register) then 
       registers.[register] 
    else 
        registers.[register] <- 0
        0

let checkCondition a b operation =
    match operation with
    | "<" -> a < b
    | ">" -> a > b
    | "<=" -> a <= b
    | ">=" -> a >= b
    | "==" -> a = b
    | "!=" -> a <> b
    | _ -> false


let execute registers (instruction: string list) =
    let targetRegister = instruction.[0]
    let sourceRegister = instruction.[4]
    let target = getRegisterValue registers targetRegister
    let source = getRegisterValue registers sourceRegister
    if checkCondition source (instruction.[6] |> int) instruction.[5] then
        let multiplier = 
            match instruction.[1] with
            | "inc" -> 1
            | "dec" -> -1
            | _ -> 0
        registers.[targetRegister] <- target + (multiplier * (instruction.[2] |> int))
        registers.[targetRegister]
    else
        0

let solve input = 
    let registers = new Dictionary<string, int>()
    let exec = execute registers

    let values = input |> Array.map (splitOnSpace >> exec)
    
    let part1 = registers |> Seq.map(|KeyValue|) |> Seq.sortByDescending snd |> Seq.head  

    (part1, values |> Array.max)  

