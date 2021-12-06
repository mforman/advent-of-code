import scala.io.Source

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
    values.flatten.filter(!_.seen).map(_.value).sum * winningDraw
  }
}

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

val fileName = "2021/04.txt"
val input = Source.fromFile(fileName).getLines().mkString("\n")
val r = """[\n\r\s]+""".r

val rawDraws :: rawBoards = input.split("\n\n").toList
val draws = rawDraws.split(",").map { _.toInt }.toList

val boards = rawBoards
  .map(s => {
    Board(r.split(s.trim).map( x => { Square(x.toInt, false) }).grouped(5).toArray)
  })

val (_, winners) = PlayNext((boards, List[WinningBoard]()), draws)

val part1 = winners.head.score
val part2 = winners.last.score
