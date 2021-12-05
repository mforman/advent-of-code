import java.io.FileNotFoundException
import scala.collection.mutable.ListBuffer
import scala.io.Source

// val input =
//   """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
//     |
//     |22 13 17 11  0
//     | 8  2 23  4 24
//     |21  9 14 16  7
//     | 6 10  3 18  5
//     | 1 12 20 15 19
//     |
//     | 3 15  0  2 22
//     | 9 18 13 17  5
//     |19  8  7 25 23
//     |20 11 10 24  4
//     |14 21 16 12  6
//     |
//     |14 21 17 24  4
//     |10 16 15  9 19
//     |18  8 23 26 20
//     |22 11 13  6  5
//     | 2  0 12  3  7""".stripMargin

val fileName = "2021/04.txt"
val input = Source.fromFile(fileName).getLines().mkString("\n")

case class Board(
    grid: Array[Array[Int]],
    seen: collection.mutable.Map[String, ListBuffer[Int]]
)
val r = """[\n\r\s]+""".r

val rawDraws :: rawBoards = input.split("\n\n").toList

val draws = rawDraws.split(",").map { _.toInt }.toList
val boards = rawBoards.map(s => {
  val items = r.split(s.trim).map { _.toInt }.toArray
  val rows = items.sliding(5, 5).toArray
  Board(
    rows,
    collection.mutable.Map
      .WithDefault(collection.mutable.Map(), k => ListBuffer())
  )
//   rows ::: rows.transpose
})

boards(0).grid.toList.map { _.toList }

def PlayBingo(boards: List[Board], draws: List[Int]): Option[(Int, Board)] = {
  draws.foreach { n =>
    boards.foreach { b =>
      b.grid.zipWithIndex
        .foreach {
          case (row, r) => {
            row.zipWithIndex
              .foreach {
                case (cell, c) => {
                  if (cell != 0 && cell == n) {
                    println(s"r$r:c$c = $cell. Target=$n")
                    val kr = "r" + r.toString
                    val kc = "c" + c.toString

                    b.seen(kr) = b.seen(kr) += cell
                    b.seen(kc) = b.seen(kc) += cell

                    b.grid(r)(c) = 0

                    if (b.seen(kr).length == 5 || b.seen(kc).length == 5) {
                      return Some((n, b))
                    }
                  }
                }
              }
          }
        }
    }
  }
  return None
}

boards(0)
val result = PlayBingo(boards, draws)
result match {
  case Some(n, board) => board.grid.map(_.sum).sum * n
}
