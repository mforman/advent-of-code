import scala.io.Source
import scala.collection.mutable

// Learning from https://github.com/lupari/aoc2021/blob/main/src/main/scala/challenge/Day15.scala


var fileName = "2021/15.txt"
var input =
  Source
    .fromFile(fileName)
    .getLines()
    .map(_.split("").map(_.toInt).toList)
    .toList

case class Point(x: Int, y: Int) {
  def adjacent: List[Point] = {
    List(Point(x, y - 1), Point(x, y + 1), Point(x - 1, y), Point(x + 1, y))
  }
}

type Grid = Map[Point, Int]

object dijkstra:
  def apply[A](start: A, goal: A)(nf: A => Iterable[A])(cf: (A,A) => Int) : (Map[A, Int], Option[(A, Int)]) =
    val seen: mutable.Map[A, Int]               = mutable.Map.empty
    val unseen: mutable.PriorityQueue[(Int, A)] = mutable.PriorityQueue.empty(Ordering.by(-_._1))
    unseen.enqueue((0, start))
    while unseen.nonEmpty do
      val (dist, node) = unseen.dequeue()
      if !seen.contains(node) then
        seen(node) = dist
        if node == goal then return (seen.toMap, Some(node -> dist))
        else
          def visit(n: A, d: Int) = 
            if !seen.contains(n) then unseen.enqueue((dist + d, n))
          nf(node).map(n => (n, cf(node, n))).foreach(n=> visit(n._1, n._2))

    (seen.toMap, None)

val grid = input.zipWithIndex
  .map {
    case (row, x) => {
      row.zipWithIndex.map {
        case (v, y) => {
          Point(x, y) -> v
        }
      }
    }
  }
  .flatten
  .toMap

def expand(g: Grid, by:Int) : Grid = {
  val end = g.keys.maxBy(p => p.x * p.y)
  val (w,h) = (end.x + 1, end.y + 1)
  List.tabulate(by, by)((x,y) => 
    g.map((k,v) => Point(x * w + k.x, y*h + k.y) -> (1 + (v - 1 + x + y) %9)))
  .flatten
  .flatten
  .toMap
}

def partOne(): Int =
  val start = Point(0,0)
  val goal = Point(grid.maxBy(_._1.x)._1.x, grid.maxBy(_._1.y)._1.y)
  def nf(p: Point) = p.adjacent.filter(grid.contains)
  def cf(a: Point, b:Point) = grid(b)
  dijkstra(start, goal)(nf)(cf)._2.get._2

def partTwo(): Int = 
  val expandedGrid = expand(grid, 5)
  val start = Point(0,0)
  val goal = Point(expandedGrid.maxBy(_._1.x)._1.x, expandedGrid.maxBy(_._1.y)._1.y)
  def nf(p: Point) = p.adjacent.filter(expandedGrid.contains)
  def cf(a: Point, b:Point) = expandedGrid(b)
  dijkstra(start, goal)(nf)(cf)._2.get._2


partOne()
partTwo()

