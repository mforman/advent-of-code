using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Advent
{
    public class OneTimeBook
    {
        static MD5 md5 = MD5.Create();
        int _stretch;
        int _window = 1000;
        string _salt;

        ConcurrentDictionary<int, string> _hashes;

        public OneTimeBook(string salt) : this(salt, 0) { }
        public OneTimeBook(string salt, int stretch)
        {
            _salt = salt;
            _stretch = stretch;
            _hashes = new ConcurrentDictionary<int, string>();
        }

        public Dictionary<int, string> Solve(int quantity)
        {
            var results = new Dictionary<int, string>();
            var index = 0;

            while (results.Count < 64)
            {
                string h;
                if (!_hashes.TryGetValue(index, out h))
                {
                    h = GetHash(index);
                    _hashes[index] = h;
                }

                var c = GetRepeats(h, 3);
                if (c.HasValue)
                {
                    var keys = Enumerable.Range(index + 1, _window).ToArray();
                    int[] buffer;
                    var tasks = new List<Task>(8);

                    for (var i = 0; i < keys.Length; i += 125)
                    {
                        buffer = new int[125];
                        Array.Copy(keys, i, buffer, 0, 125);
                        tasks.Add(GetHashesBatch(buffer));
                    }

                    Task.WaitAll(tasks.ToArray());

                    for(var i = index + 1; i <= index + _window; i++)
                    {
                        string nextHash;
                        if (!_hashes.TryGetValue(i, out nextHash))
                        {
                            nextHash = GetHash(i);
                            _hashes[i] = nextHash;
                        }

                        var match = GetRepeats(nextHash, 5, c);
                        if (match.HasValue)
                        {
                            Console.WriteLine($"{index} {h}");
                            results[index] = h;
                            break;
                        }
                    }
                }

                index += 1;

                var oldKeys = _hashes.Keys.Where(k => k < index).ToList();
                string s;
                foreach(var k in oldKeys)
                {
                    _hashes.TryRemove(k, out s);
                }
            }

            return results;
        }

        private string GetHash(int index)
        {
            var s = $"{_salt}{index}";
            for(var i = 0; i < _stretch + 1; i++)
            {
                s = GetHash(s);
            }
            return s;
        }

        private string GetHash(string item)
        {
            var b = Encoding.UTF8.GetBytes(item);
            var h = md5.ComputeHash(b);
            var sb = new StringBuilder(h.Length * 2);
            for (var i = 0; i < h.Length; i++)
            {
                sb.Append(h[i].ToString("x2"));
            }
            return sb.ToString();
        }

        private async Task GetHashesBatch(int[] indexes)
        {
            await Task.CompletedTask;
            var result = new Dictionary<int, string>(indexes.Length);
            foreach(var i in indexes)
            {
                if (_hashes.ContainsKey(i))
                {
                    continue;
                }
                _hashes[i] = GetHash(i);
            }
        }

        private char? GetRepeats(string item, int length, char? targetChar = null)
        {
            if (item.Length < length)
            {
                return null;
            }
            for (var i = length - 1; i < item.Length; i++)
            {
                var segment = item.Substring(i - (length - 1), length).ToCharArray();
                if (segment.Distinct().Count() == 1 && (!targetChar.HasValue || targetChar == segment[0]))
                {
                    return segment[0];
                }
            }
            return null;
        }
    }
    public class Program
    {
        public static void Main(string[] args)
        {
            // var partOne = new OneTimeBook("qzyelonm", 0);

            // var swOne = Stopwatch.StartNew();
            // var one = partOne.Solve(64);
            // swOne.Stop();

            // Console.WriteLine($"Part 1: {one.Keys.OrderByDescending(k => k).First()} - {one.Count} hashes in {swOne.ElapsedMilliseconds} ms");

            var partTwo = new OneTimeBook("abc", 2016);

            Console.WriteLine("");

            var swTwo = Stopwatch.StartNew();
            var two = partTwo.Solve(64);
            swTwo.Stop();

            Console.WriteLine($"Part 2: {two.Keys.OrderByDescending(k => k).First()} - {two.Count} hashes in {swTwo.ElapsedMilliseconds} ms");
        }
    }
}
