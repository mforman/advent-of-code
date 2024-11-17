// Part 1
let getLevel (i:int) = 
    i 
    |> (float)
    |> sqrt 
    |> ceil 
    |> int
    |> (fun x -> if x % 2 = 1 then x else x + 1)

let getCenters (i:int) =
    [0..3]
    |>List.map (fun x -> ((i*i) - (i/2)) - ((i-1)*x))
    
let getCorners (i:int) =
    [0..3]
    |> List.map (fun x -> (i*i) - ((i-1) * x))
    |> List.rev


let solve1a (i:int) =
    let level = getLevel i
    let centers = getCenters level
    let stepsToCenter = centers |> List.map (fun x -> abs(i - x)) |> List.min
    stepsToCenter + (level / 2)

// Part 2
type Point = {
    x : int
    y : int
}
with static member (+) (a:Point, b:Point) = { x = a.x + b.x; y = a.y + b.y }

type Storage = {
    i: int
    point : Point
    value : int
}

let getStorageHead (s:Storage list) = 
    s |> List.sortBy (fun x -> x.i) |> List.last

let turn (n:int) =
    ((((n*4)+1 |> float |> sqrt |> floor |> int) + 3) % 4) + 1

let move (p:Point) (direction:int) =
    let x = 
        match direction with 
        | 1 -> { x = 1; y = 0; }
        | 2 -> { x = 0; y = 1; }
        | 3 -> { x = -1; y = 0; }
        | 4 -> { x = 0; y = -1;}
        | _ -> { x = 0;y = 0; }
    p + x

let allAdjacent = 
    let num = [-1..1]
    num
    |> List.collect (fun i -> num |> List.map (fun j -> { x=i; y=j; }) )

let getAdjacentPoints p =
    allAdjacent |> List.map (fun x -> x + p)
let rec advance (storage:Storage list) =
    let current = storage |> getStorageHead
    
    let nextIndex = current.i + 1
    let currentLevel = getLevel current.i
    let nextLevel = getLevel nextIndex

    let nextPoint = move current.point (turn (current.i-1))
    
    let adjacent = getAdjacentPoints nextPoint
    
    let nextValue = 
        storage 
        |> List.filter (fun s -> List.contains s.point adjacent)
        |> List.sumBy (fun s -> s.value)

    let nextItem =
        { 
            i = nextIndex;
            point = nextPoint;
            value = nextValue;
        }
    
    storage |> List.append [nextItem]

let rec advanceUntil (storage:Storage list) (stopAt:int) =
    let current = storage |> getStorageHead
    if current.value > stopAt then
        current
    else
        let next = advance storage
        let h = next |> getStorageHead
        if h.value > stopAt then
            h
        else advanceUntil next stopAt


let init = [{ i=1; point={x=0;y=0}; value=1;}]
