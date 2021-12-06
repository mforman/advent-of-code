// import scala.collection.mutable.Buffer
import scala.io.Source
import scala.collection

// def nextDay(items: Vector[Int]): Vector[Int] = {
//   val adds = items.count(_ == 0)
//   items.map(n => {
//     n match {
//       case 0 => 6
//       case _ => n - 1
//     }
//   }) ++ Vector.fill(adds)(8)
// }

// def nextDayMutable(items: Buffer[Int]): Unit = {
//   (0 until items.length).foreach(i => {
//     val x = items(i)
//     x match {
//       case 0 => {
//         items(i) = 6
//         items.append(8)
//       }
//       case _ => items(i) -= 1
//     }
//   })
// }

// val input = "3,4,3,1,2"
val fileName = "2021/06.txt"
val input = Source.fromFile(fileName).mkString
val nums = input.split(",").map(_.toInt).toBuffer

val emptyMap = (0L to 8L).map(_ -> 0L).toMap
val fishMap = nums.foldLeft(emptyMap)((acc, n) => acc.updated(n, acc(n) + 1))

def nextDay(items: Map[Long, Long]): Map[Long, Long] = {
  val rotated = items.map { case (k, v) => k - 1 -> v }
  val updated =
    Map(-1L -> 0L, 6L -> (rotated(6L) + rotated(-1L)), 8L -> (rotated(-1L)))
  rotated ++ updated
}

def process(n: Int): Map[Long, Long] =
  (0 until n).foldLeft(fishMap)((acc, _) => nextDay(acc))

process(80).values.sum
process(256).values.sum
// // (1 to 80).foldLeft(nums)((acc, elem) => nextDay(acc)).length
// (1 to 256).foreach(i => { nextDayMutable(nums) })
// nums.length
