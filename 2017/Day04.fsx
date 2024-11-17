    open System
    let readLines filePath = System.IO.File.ReadLines(filePath)
    let lines = readLines "2017\\04\\input.txt"
    let parseLine (s:string) = 
        s.Split() 
        |> Array.filter (fun x -> x.Length > 0)
        |> Array.toSeq

    let isUnique (s:string seq) =
        s
        |> Seq.groupBy (id)
        |> Seq.exists (fun (_, y) -> (y |> Seq.length) > 1)
        |> not
    
    let sortAllStrings (s:string seq) = s |> Seq.map (Seq.sort >> Seq.toArray >> System.String)

    let isValid s = isUnique s && isUnique (sortAllStrings s)

    let sample = [|"aa bb cc dd ee"; "aa bb cc dd aa"; "aa bb cc dd aaa"|] |> Seq.map parseLine
    let input = lines |> Seq.map parseLine




    