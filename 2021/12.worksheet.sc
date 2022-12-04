import scala.io.Source

var fileName = "2021/12.txt"
var graph =
  Source
    .fromFile(fileName)
    .getLines()
    .flatMap(x =>
      x.split("-") match {
        case Array(a, b) => Array(a -> b, b -> a)
      }
    )
    .filterNot((a, b) => a == "end" || b == "start")
    .toList
    .groupMap(_._1)(_._2)
    .toMap ++ Map("end" -> List())

def isSmall(s: String): Boolean = s.equals(s.toLowerCase)

def search(current: String, visited: Set[String], singleVisit: Boolean): Int = {
  current match {
    case "end" => 1
    case _
        if visited.contains(current) && (singleVisit || current == "start") =>
      0 // dead end
    case _ => {
      val updatedSingleVisit = visited.contains(current) || singleVisit

      val updatedVisited = isSmall(current) match {
        case true  => visited + current
        case false => visited
      }

      graph(current)
        .map(search(_, updatedVisited, updatedSingleVisit))
        .sum
    }
  }
}

val part1 = search("start", Set(), true)
val part2 = search("start", Set(), false)

// val emptyMap = Map[String, List[String]]().withDefaultValue(List())

// val graph = input.foldLeft(emptyMap)((acc, elem) => {
//   val (a, b) = elem
//   val mapA = Map(a -> (acc(a) :+ b))
//   val mapB = Map(b -> (acc(b) :+ a))
//   acc ++ mapA ++ mapB
// })

// def traverse(current: String, seen: Set[String], paths: Int): Int = {
//   if (current == "end") paths + 1
//   else {
//     graph(current)
//       .filterNot(seen)
//       .map { cave =>
//         val nextSeen = if (isSmall(cave)) seen + cave else seen
//         traverse(cave, nextSeen, paths)
//       }
//       .sum
//   }
// }
// traverse("start", Set("start"), 0)

// // val start = "start"
// // val path = List[String]()
// // graph(start).map(x => path :+ x)
// // dfs(start, graph)
