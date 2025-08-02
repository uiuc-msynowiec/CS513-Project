using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Text.RegularExpressions;

namespace condense_mass_edits
{
    internal class Program
    {
        class Operation
        {
            public List<string> value = new List<string>();

            public bool IsMassEdit()
            {
                return Title.StartsWith("mass-edit");
            }
            public string Title { get; set; }
            public string InTable { get; set; }
            public string OutTable { get; set; }

            public string Param { get; set; }

            public bool CombineWithLast(Operation last)
            {
                if (last.Param == Param)
                {
                    InTable = last.InTable;
                    return true;
                }
                return false;
            }

            public void Write(StreamWriter sw)
            {
                if (IsMassEdit())
                {
                    sw.WriteLine($"#@begin core/{Title}#@desc Mass edit cells in column place_cleaned");
                    sw.WriteLine("#@param col-name:place_cleaned");
                    sw.WriteLine($"#@in {InTable}");
                    sw.WriteLine($"#@out {OutTable}");
                    sw.WriteLine($"#@end core/{Title}");
                    //#@begin core/mass-edit3#@desc Mass edit cells in column place_cleaned
                    //#@param col-name:place_cleaned
                    //#@in table6
                    //#@out table7
                    //#@end core/mass-edit3
                }
                else
                {
                    foreach (var line in value)
                    {
                        sw.WriteLine(line);
                    }
                }
            }
        }

        static Operation ReadOperation(ref int line, string[] lines, StreamWriter sw)
        {
            //#@begin core/mass-edit72#@desc Mass edit cells in column place_cleaned
            var m = Regex.Match(lines[line], "^#@begin core\\/([^#]+)#");
            if (m.Success)
            {
                Operation op = new Operation()
                {
                    Title = m.Groups[1].Value
                };
                op.value.Add(lines[line]);
                line++;
                while (!lines[line].StartsWith("#@end"))
                {
                    op.value.Add(lines[line]);

                    if (op.Title.StartsWith("mass-edit"))
                    {
                        var io = Regex.Match(lines[line], "^#@(in|out) (.+)$");
                        if (io.Success)
                        {
                            switch (io.Groups[1].Value)
                            {
                                case "in":
                                    op.InTable = io.Groups[2].Value;
                                    break;
                                case "out":
                                    op.OutTable = io.Groups[2].Value;
                                    break;
                                default:
                                    break;
                            }
                        }

//#@begin core/mass-edit3#@desc Mass edit cells in column place_cleaned
//#@param col-name:place_cleaned
//#@in table6
//#@out table7
//#@end core/mass-edit3
                    }

                    line++;
                }
                op.value.Add(lines[line]);
                line++;

                return op;
            }
            else
            {
                sw.WriteLine(lines[line++]);
                //throw new NotSupportedException($"unexpected on line {line}: {lines[line]}");
            }
            return null;
        }

        static void Main(string[] args)
        {
            var lines = File.ReadAllLines(args[0]);

            using (StreamWriter sw = new StreamWriter($"{args[0]}.out.yw"))
            {

                int index = 0;
                Operation last = null;
                while (index < lines.Length)
                {
                    var op = ReadOperation(ref index, lines, sw);

                    if (op != null)
                    {

                        bool writeLast = true;
                        if (op.IsMassEdit())
                        {
                            if (last != null &&
                                last.IsMassEdit())
                            {
                                writeLast = false;
                                if (!op.CombineWithLast(last))
                                {
                                    writeLast = true;
                                }
                            }
                        }

                        if (writeLast && last != null)
                        {
                            last.Write(sw);
                        }
                    }

                    last = op;
                }

                last?.Write(sw);
            }
        }
    }
}
