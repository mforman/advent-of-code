#load "common.fsx"
open Common

type Mode = Normal | Garbage | Cancelled
type StreamState = {
    mode: Mode
    total: int
    currentGroup: int
    garbageCount: int
}

let processChar c state =
    match (state.mode, c) with
    | (Cancelled, _) | (Normal, '<' ) -> { state with mode = Garbage }
    | (Garbage, '>') -> { state with mode = Normal }
    | (Garbage, '!') -> { state with mode = Cancelled }
    | (Garbage, _) -> { state with garbageCount = state.garbageCount + 1 }
    | (Normal, '{') -> { state with currentGroup = state.currentGroup + 1 }
    | (Normal, '}') -> { state with 
                            total = state.total + state.currentGroup; 
                            currentGroup = state.currentGroup - 1}
    | (_, _) -> state
    
    // if state.InGarbage && state.IgnoreNext then
    //     { state with IgnoreNext = false }
    // elif state.InGarbage then
    //     match c with
    //     | '>' -> { state with mode = Normal }
    //     | '!' -> { state with mode = Cancelled }
    //     | _ -> { state with garbageCount = state.garbageCount + 1 }
    // else // Not in garbage
    //     match c with
    //     | '<' -> { state with mode = Garbage }
    //     | '{' -> { state with currentGroup = state.currentGroup + 1 }
    //     | '}' -> { state with 
    //                 total = state.total + state.currentGroup; 
    //                 currentGroup = state.currentGroup - 1 
    //              }
    //     | _ -> state
        

let processStream (input:string) =
    let initialState = { mode = Normal; total = 0; currentGroup = 0; garbageCount = 0; }
    let finalState = input |> Seq.fold (fun acc elem -> processChar elem acc) initialState
    finalState