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

case class Square(value:Int, seen:Boolean)
class Board(var values: Array[Array[Square]]):
    def play(draw:Int) : Board = {
      this match {
        case _: WinningBoard => this
        case _ => {
          val newBoard = Board(values.flatten.map(s => Square(s.value, s.seen || s.value == draw)).grouped(5).toArray)
          newBoard.hasBingo match {
            case true => WinningBoard(newBoard.values, draw)
            case false => newBoard
          } 
        }  
      }    
    }
    var hasBingo : Boolean = {
      val allSeen = (a:Array[Square]) => a.forall(_.seen)
      values.exists(allSeen) || values.transpose.exists(allSeen)
    }
class WinningBoard(values: Array[Array[Square]], var winningDraw: Int) extends Board(values) {
  var score:Int = {
    values.flatten.filter(s=>s.seen == false).map(s => s.value).sum * winningDraw
  }
}

val r = """[\n\r\s]+""".r

val rawDraws :: rawBoards = input.split("\n\n").toList
val draws = rawDraws.split(",").map { _.toInt }.toList

val boards = rawBoards
  .map(s => {
    Board(r.split(s.trim).map( x => { Square(x.toInt, false) }).grouped(5).toArray)
  })


def PlayNext(boards:(List[Board],List[WinningBoard]), draws:List[Int]) : (List[Board],List[WinningBoard]) = {
  val draw :: remainingDraws = draws
  val nextBoards = boards._1.map(_.play(draw))
  val winners = boards._2
  val (newWinners, remainingBoards) = nextBoards.partition{case x: WinningBoard => true case _ => false}
  val result = (remainingBoards, winners:::(newWinners.map(_.asInstanceOf[WinningBoard])))
  if (remainingBoards.length == 0 || remainingDraws.length == 0){
    result
  } else {
    PlayNext(result, remainingDraws)
  }
}

val (_, winners) = PlayNext((boards, List[WinningBoard]()), draws)

val part1 = winners.head.score
val part2 = winners.last.score