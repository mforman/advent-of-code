module Common

open System.Text.RegularExpressions

let readLines fileName = System.IO.File.ReadAllLines(fileName)
let readAll fileName = System.IO.File.ReadAllText(fileName)

let parseList fn (str: string) =
    str.Split([|'\t'; ' '; '\r'; '\n';|])
    |> Array.choose (fun e ->
        match e.Trim() with
        | "" -> None
        | e -> Some (fn e))

let parseLines (str: string) =
    str.Split([|'\r'; '\n'|])
   |> Array.choose (fun row ->
        match row.Trim() with
        | "" -> None
        | row -> Some row)

let parseMatrix fn str =
   str
   |> parseLines
   |> Array.map (parseList fn)
   |> Array.filter (not << Array.isEmpty)


let (|Regex|_|) pattern input =
        let m = Regex.Match(input, pattern)
        if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
        else None