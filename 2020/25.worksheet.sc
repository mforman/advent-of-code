val card = 5764801L
val door = 17807724L

def transform(subject: Int, loopSize: Int): Long = {
  (1 to loopSize) fold(1) {
    (acc, _) => (acc * subject).toLong % 20201227
}

def findLoopSize(subject: Int, pubKey: Long): Option[Int] =
  LazyList.from(0) find {
    transform(subject, _) == pubKey
  }

val cardLoop = findLoopSize(7, card)
