    let readLines filePath = System.IO.File.ReadLines(filePath)
    let lines = readLines "2017\\02\\input.txt"
    let parseLine (s:string) = 
        s.Split() 
        |> Array.filter (fun x -> x.Length > 0)
        |> Array.map int

    let parsed = lines |> Seq.map parseLine

    let greatestDifferece (items:int []) = (Array.max items) - (Array.min items)

    let evenDivide (items:int []) = 
        let result = 
            items
            |> Array.collect (fun i -> items 
                                    |> Array.map (fun x -> (i, x)) 
                                    |> Array.filter (fun (x,y) -> x<>y))
            |> Array.tryPick (fun (i,j) -> if i % j = 0 then Some (i / j) else None)

        match result with
        | Some i -> i
        | _ -> 0

    let result1 = parsed |> Seq.sumBy(greatestDifferece)
    let result2 = parsed |> Seq.sumBy(evenDivide)
