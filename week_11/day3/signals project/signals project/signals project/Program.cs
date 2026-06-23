using System;


namespace day3
{

    enum classifications
    {
        Friendly
               , Hostile,
        Unidentified
    }
    class signalss
    {
        static void ShowAllSignal(List<int> id, List<string> classification, List<int> siganls)
        {
            for (int i = 0; i < id.Count; i++)
            {
                if (siganls[i] == -1)
                {
                    Console.WriteLine($"id: {id[i]} classification: {classification[i]} signal: unknown (no reading)");
                }
                else
                {
                    Console.WriteLine($"id: {id[i]} classification: {classification[i]} signal: {siganls[i]}");
                }
            }

        }

        static void AddTranmission(List<int> id, List<string> classification, List<int> siganls)
        {

            //need secure function that only numbers allowed else error
            //user input here
            int userId = int.Parse("1");
            string userClassififcation = "Unidentified";
            string usersignal = Console.ReadLine();
            if (usersignal.Length == 0)
            {
                int userSignal = -1;
                siganls.Add(userSignal);
                id.Add(userId);
                classification.Add(userClassififcation);
            }
            else
            {
                int usersignalint = int.Parse(usersignal);
                id.Add(userId);
                classification.Add(userClassififcation);
                siganls.Add(usersignalint);
            }    
            
          



        }


        static void calibrate(int userid,int newSignal, List<int> id, List<int> siganls)
        {
            for (int i = 0; i < id.Count; i++)
               {
                if (userid == id[i])
                    siganls[i] = newSignal;
                    break;
                }
        }


        static void Main()
        {
            List<int> id = new List<int>();
            List<string> classification = new List<string>();
            List<int> siganls = new List<int>();
            ShowAllSignal( id,  classification,  siganls);
            AddTranmission(id, classification, siganls);
            ShowAllSignal(id, classification, siganls);
            calibrate(1, 10, id, siganls);
            ShowAllSignal(id, classification, siganls);

        }


    }
        
        
    
    
}