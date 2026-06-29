using System;

namespace project
{
    abstract class Platform
    {
        protected int TrackId { get; }
        protected double SpeedKnots;
        
        
        
        protected double speedknots
        {
            get=> SpeedKnots;
            set
            {
                if (value < 0) SpeedKnots = 0;
                else SpeedKnots = value;
            }
        }
        protected double Heading;

        protected double heading
        {
            get => Heading;
            set
            {
                if (0 > value || value > 359) Heading = 0;
                else Heading = value;
            }
        }

        protected Platform(int trackId, double speedknotss,double headingg )
        {
            TrackId = trackId;
            speedknots = speedknotss;
            heading = headingg;
        }

        public abstract string StatusLine();
        public abstract bool IsTrackable();
        public override string ToString()
        => $"trackid : {TrackId} speedkonts : {speedknots} heading : {heading}";
    }

    class AirPlatform : Platform
    {
        protected double AltitudeFeet;


         public override string StatusLine()
          => $"AltitudeFeet:{AltitudeFeet}";

        public override bool IsTrackable()
        {
            if (100 < AltitudeFeet && 60000 > AltitudeFeet && SpeedKnots > 0) return true;
            else return false;
        }

        public AirPlatform( int trackId, double speedknots, double heading ,double altitudeFeet) :base( trackId,speedknots,heading)
        { 
            AltitudeFeet = altitudeFeet;
        }
    
    
    
    
    }

    class SeaPlatform : Platform
    {
        protected double DepthMeters;


        public SeaPlatform(int trackId, double speedknots, double heading, double depthMeters) : base(trackId, speedknots, heading)
        {
            DepthMeters = depthMeters;
        }


        public override string StatusLine()
         => $"DepthMeters:{DepthMeters}";
        public override bool IsTrackable()
        {
            if (0 < DepthMeters && DepthMeters < 300) return true;
            else return false;
        }
        
    }

    class GroundPlatform : Platform
    {
        protected string TerrainType;

        public GroundPlatform(int trackId, double speedknots, double heading, string terraintype) : base(trackId, speedknots, heading)
        {
            TerrainType = terraintype;
        }

        public override string StatusLine()
        => $"TerrainType:{TerrainType}";
        public override bool IsTrackable()
        {
            if ( TerrainType != "tunnel") return true;
            else return false;
        }



    }

    class M
    {
        static void Main()
        {
            AirPlatform a = new AirPlatform(1, 101, 100, 122);
            GroundPlatform b = new GroundPlatform(2, 102, 202, "highway");
            SeaPlatform c = new SeaPlatform(3, 103, 203, -1);
            
            Console.WriteLine(a.IsTrackable());
            List<Platform> platforms = [a,b,c];
            foreach (Platform objectd in platforms)
            {
                Console.WriteLine($"{objectd.StatusLine()} {objectd.ToString()} {objectd.IsTrackable()}");
            }
        }
    }


}