let modulo = 2147483647L

let generator (factor : int64) (init : int64) : int64 seq =
    Seq.unfold (
        fun n ->
            let n' = n * factor % modulo
            Some (n', n')
    ) init

let nbSimilarities genA genB n =
    Seq.zip genA genB
    |> Seq.take n
    |> Seq.fold (fun s (a, b) -> s + if int16 a = int16 b then 1 else 0) 0

let nbSimilarities1 (a : int64) (b : int64) =
    nbSimilarities (generator 16807L a) (generator 48271L b) 40000000

let nbSimilarities2 (a : int64) (b : int64) =
    let genA = generator 16807L a |> Seq.filter (fun v -> v % 4L = 0L)
    let genB = generator 48271L b |> Seq.filter (fun v -> v % 8L = 0L)
    nbSimilarities genA genB 5000000