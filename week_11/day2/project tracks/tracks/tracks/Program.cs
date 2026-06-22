using System;
using System.Runtime.CompilerServices;


namespace main
{
    class Tracks
    {
         

        static void Main()
        {
            List<int> idList = new List<int>();
            List<int> speedList = new List<int>();
            List<int> headingList = new List<int>();


            bool flag = true;
            while (flag) 
            {
                ShowMenu();
                string menuInput = Console.ReadLine();
                switch (menuInput)
                {
                    case "1":
                      AddTruck(idList, speedList, headingList);
                        break;
                    
                    case "2":
                        string inputId = Console.ReadLine();
                        int id = int.Parse(inputId);
                        RemoveTruckByID(id, idList, speedList, headingList);
                        break;
                    
                    case "3":
                        string inputId2 = Console.ReadLine();
                        int id2 = int.Parse(inputId2);
                        FindTruck(id2, idList, speedList, headingList);
                        break;

                    case "4":
                        AllTrucks(idList, speedList, headingList);
                        break;
                    
                    case "5":
                        string inputSpeed = Console.ReadLine();
                        int speed = int.Parse(inputSpeed);
                        AllTrucks(speed, idList, speedList, headingList);
                        break;
                    
                    case "6":
                        Console.WriteLine(Summarize(idList, speedList, headingList));
                        break;
                    
                    case "7":
                        break;



                }
                
            }
            
            
            
            //AddTruck(idList, speedList, headingList);
            //FindTruck(54, idList, speedList, headingList);
            //AllTrucks(idList,speedList,headingList);
            //RemoveTruckByID(1,idList,speedList,headingList);
            //AllTrucks(idList, speedList, headingList);



        }

        static void ShowMenu()
        {
        Console.WriteLine("""
            
            WELCOM TO TRUCKS SYSTEM
            
            MENU (1 - 7)
            1:add truck
            2:remove truck 
            3:find truck by id
            4:show all trucks
            5:filter trucks by speed
            6:summerize trucks
            7:quit 
            
            enter only 1 - 7 numbers:
            """);
        }

        static List<int> TruckUser()   //add error hanedeling
        {
            bool flug = true;
            //while TRUE
            
            
            string idUser = Console.ReadLine();
            string speedUser = Console.ReadLine();
            string headingUser = Console.ReadLine();
            
            //FUNCTION CHECK AND RETURN TRUE OR FALSE IF CHECK GOOD


            int id = int.Parse(idUser);
            int speed = int.Parse(speedUser);
            int heading = int.Parse(headingUser);

            return [id, speed, heading];

        }



        static void AddTruck(List<int> idList, List<int> speedList, List<int> headingList)
        {
            //the function return list of tree values user (id , speed , heading)
            List<int> listUser = TruckUser();
            
            int id = listUser[0];
            int speed = listUser[1];
            int heading = listUser[2];
            
      
            idList.Add(id);
            speedList.Add(speed);
            headingList.Add(heading);

            Console.WriteLine("\nsuccess to add");
        }


        static void RemoveTruckByID(int id,List<int> idList , List<int> speedList, List<int> headingList)
        {
            for (int i = 0; i < idList.Count; i++)
            {
                if (idList[i] == id)
                {
                    int index = i;
                    idList.RemoveAt(i);
                    speedList.RemoveAt(i);
                    headingList.RemoveAt(i);
                    Console.WriteLine("\nsuccess to remove");
                    break;
                }
            }
            Console.WriteLine("\n id not found");
        }

        static void AllTrucks(List<int> idList, List<int> speedList, List<int> headingList)
        {
            
            for (int i = 0;i < idList.Count; i++)
            {
                Console.WriteLine($"id: {idList[i]} speed: {speedList[i]} heading: {headingList[i]}");
            }
            if (idList.Count == 0) Console.WriteLine("empty");
        }

        static void FindTruck(int id, List<int> idList, List<int> speedList, List<int> headingList)
        {
             for (int i = 0;i < idList.Count;i++ )
            {
                if (idList[i] == id)
                {
                    int index = i;
                    Console.WriteLine($"id: {idList[i]} speed: {speedList[i]} heading: {headingList[i]}");
                    return;
                }
            }
            Console.WriteLine("id not found");
        }

        static void AllTrucks(int speed, List<int> idList, List<int> speedList, List<int> headingList)
        {
            List<string> matchSpeed = new List<string>();
            for (int i = 0; i < speedList.Count; i++)
            {
                if (speedList[i]>= speed)
                {
                    matchSpeed.Add($"id: {idList[i]} speed: {speedList[i]} heading: {headingList[i]}");
                }
                
            }
            foreach (string v in matchSpeed) Console.WriteLine(v);
                
        }

        static string Summarize(List<int> idList, List<int> speedList, List<int> headingList)
        {
            int count = idList.Count;
            int avrage = speedList.Sum() / count;
            int maxSpeed = speedList.Max();
            int indexFastest = speedList.IndexOf(maxSpeed);
            string fastestTruck = $"id: {idList[indexFastest]} max speed: {speedList[indexFastest]} heading: {headingList[indexFastest]}"; 
            return $"count: {count} avrage: {avrage}\nthe fastest truck is {fastestTruck}";
        }

        



    }
}