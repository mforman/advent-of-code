import scala.annotation.tailrec
import scala.io.Source

// val input = List(
//   "00100",
//   "11110",
//   "10110",
//   "10111",
//   "10101",
//   "01111",
//   "00111",
//   "11100",
//   "10000",
//   "11001",
//   "00010",
//   "01010"
// )

def GetPowerConsumption(items: List[String]): Int = {
  items
    .map(s => { s.reverse })
    .map(s => { s.toCharArray.map(c => c.toString.toInt).toList })
    .transpose
    .zipWithIndex
    .map {
      case (x, i) => {
        val a = math.pow(2, i).toInt
        val mostFrequent =
          x.groupMapReduce(identity)(_ => 1)(_ + _).maxBy(_._2)._1
        mostFrequent match {
          case 1 => List(a, 0)
          case _ => List(0, a)
        }
      }
    }
    .transpose
    .map(x => x.sum)
    .product
}

@tailrec
private def FindRatingAtPosition(
    items: List[String],
    mode: Int,
    position: Int
): Int = {
  items.length match {
    case 1 => Integer.parseInt(items.head, 2)
    case _ => {
      val counts = items
        .map(s => s.charAt(position))
        .groupMapReduce(identity)(_ => 1)(_ + _)

      val (a, b) = (counts('0'), counts('1'))
      val f = mode match {
        case 1 => if (b >= a) '1' else '0'
        case 0 => if (a <= b) '0' else '1'
      }

      val filtered = items.filter(x => x.charAt(position) == f)
      FindRatingAtPosition(filtered, mode, position + 1)
    }
  }
}

def FindRating(
    items: List[String],
    mode: Int
): Int = FindRatingAtPosition(items, mode, 0)

def GetLifeSupportRating(items: List[String]): Int = {
  (0 to 1).map(x => FindRating(items, x)).product
}

val fileName = "2021/03.txt"
val input = Source.fromFile(fileName).getLines().toList

val part1 = GetPowerConsumption(input)
val part2 = GetLifeSupportRating(input)
