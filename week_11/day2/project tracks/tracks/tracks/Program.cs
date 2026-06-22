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
            ShowMenu();
            AddTruck(idList, speedList, headingList);
            FindTruck(54, idList, speedList, headingList);
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
            5:summerize trucks
            6:quit 
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
                if (idList[i] == id) ; int index = i;

                idList.RemoveAt(i);
                speedList.RemoveAt(i);
                headingList.RemoveAt(i);
                break;
            }
            Console.WriteLine("\nsuccess to remove");
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



    }
}