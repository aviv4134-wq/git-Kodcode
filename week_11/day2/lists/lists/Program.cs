using System;
using System.Globalization;
using System.Reflection.Metadata;
using System.Xml;

namespace day2
{
    class lists
    {
        static List<string> tracks = new List<string>();
        static List<double> speeds = new List<double>();

        static void ADDTrack(string id, double speed)
        {
            tracks.Add(id);
            speeds.Add(speed);

        }
        static double AvrageSpeed()
        {
            if (speeds.Count == 0) return 0.0;
            double sum = 0;
            foreach (double s in speeds) sum += s;
            return sum/ speeds.Count;

        }

        static void Main()
        {
            ADDTrack("1", 100);
            ADDTrack("10", 10);
            Report("10");

        }

        static void Report() // version 1: no parameters
        
        { 
            Console.WriteLine($"{tracks.Count} tracks");
        }
        
        static void Report(string id) // version 2: one string

        {
            int i = tracks.IndexOf(id);
            if (i >= 0) Console.WriteLine($"{id}: {speeds[i]} kn");
            else Console.WriteLine("id not fount"); ;
                     
        }
        
               

        
        
    }
}