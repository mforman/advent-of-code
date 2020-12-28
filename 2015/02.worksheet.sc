import scala.io.Source

val Box = """(\d+)""".r

def perms[T](elems: Seq[T], n: Int): Seq[Seq[T]] = {
  val len = elems.length
  (0 to len - 1)
    .map(i => (0 to n - 1).map(j => elems((i + j) % len)))
}

def area(elems: Array[Int]): Int = {
  val sides = perms(elems, 2)
    .map(x => x.product)

  val smallest = sides.min

  sides.fold(smallest)((acc, i) => { acc + (2 * i) })
}

def ribbon(elems: Array[Int]): Int = {
  val volume = elems.product
  val len = elems.sorted
    .take(2)
    .map(i => i * 2)
    .sum

  volume + len
}

assert(area(Array(2, 3, 4)) == 58)
assert(area(Array(1, 1, 10)) == 43)

val fileName = "2015/02.txt"
val input = Source
  .fromFile(fileName)
  .getLines()
  .toArray
  .map(x => Box.findAllIn(x) map (_.toInt) toArray)

input
  .map(area)
  .sum

input
  .map(ribbon)
  .sum
