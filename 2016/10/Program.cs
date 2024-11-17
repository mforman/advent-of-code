using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace ConsoleApplication
{
    public abstract class Bin
    {
        public static T Create<T>(int id)
        where T : Bin
        {
            var type = typeof(T);
            if (type == typeof(Bot))
            {
                return new Bot(id) as T;
            }
            if (type == typeof(Output))
            {
                return new Output(id) as T;
            }
            throw new ArgumentOutOfRangeException("Unknown type of Bin", nameof(type));
        }
        protected readonly List<int> _items;
        protected Bin(int id)
        {
            Id = id;
            _items = new List<int>();
        }
        public int Id { get; }
        public IEnumerable<int> Items 
        {
            get { return _items; }
        }

        public virtual void Add(int value)
        {
            _items.Add(value);
            //Console.WriteLine($"Added {value} to {this.GetType().Name} {Id}");
        }
    }

    public class Output : Bin 
    {
        public Output(int id) : base(id) { }
    }

    public class Bot : Bin
    {
        public Bot(int id) : base(id) { }
        public Action<int> Low { get; set; }
        public Action<int> High { get; set; }

        public override void Add(int value)
        {
            base.Add(value);
            Execute();
        }

        private void Execute()
        {
            if (this.Low == null || this.High == null || _items.Count != 2)
            {
                return;
            }
            var sorted = _items.OrderBy(x => x).ToArray();
            if (sorted[0] == 17 && sorted[1] == 61)
            {
                Console.WriteLine($"Bot {this.Id} is comparing {sorted[0]} and {sorted[1]}");
            }
            Low(sorted[0]);
            High(sorted[1]);
            _items.Clear();
        }
    }

    public static class BinExtensions
    {
        public static T GetOrCreate<T>(this Dictionary<int, T> items, int id)
            where T : Bin
        {
            if (items.ContainsKey(id))
            {
                return items.First(i => i.Key == id).Value as T;
            }
            var bin = Bin.Create<T>(id);
            // Console.WriteLine($"Created {typeof(T).Name} {id}");
            items[id] = bin;
            return bin;
        }
    }
    public class Program
    {
        public static void Main(string[] args)
        {
            var instructions = File.ReadLines("input.txt");

            var bots = new Dictionary<int, Bot>();
            var outputs = new Dictionary<int, Output>();

            foreach(var i in instructions)
            {
                // Console.WriteLine(i);
                var seg = i.Split(' ');
                int botId;
                Bot bot;
                switch(seg[0])
                {
                    case "bot":
                        botId = int.Parse(seg[1]);
                        var lowId = int.Parse(seg[6]);
                        var highId = int.Parse(seg[11]);
                        Bin low;
                        Bin high;
                        bot = bots.GetOrCreate(botId);
                        if (seg[5] == "bot")
                        {
                            low = bots.GetOrCreate(lowId);
                        }
                        else
                        {
                            low = outputs.GetOrCreate(lowId);
                        }
                        if (seg[10] == "bot")
                        {
                            high = bots.GetOrCreate(highId);
                        }
                        else
                        {
                            high = outputs.GetOrCreate(highId);
                        }
                        bot.Low = low.Add;
                        bot.High = high.Add;
                        break;
                    case "value":
                        botId = int.Parse(seg[5]);
                        var value = int.Parse(seg[1]);
                        bot = bots.GetOrCreate(botId);
                        bot.Add(value);
                        break;
                    default:
                        throw new ArgumentOutOfRangeException("Unknown instruction type");
                }
            }

            // foreach(var b in bots.OrderBy(x => x.Key))
            // {
            //     Console.Write($"Bot {b.Key}: ");
            //     foreach (var i in b.Value.Items)
            //     {
            //         Console.Write($"{i} ");
            //     }
            //     Console.Write("\n");
            // }

            foreach (var o in outputs.OrderBy(x => x.Key))
            {
                Console.Write($"Bin {o.Key}: ");
                foreach (var i in o.Value.Items)
                {
                    Console.Write($"{i} ");
                }
                Console.Write("\n");
            }
        }
    }
}
