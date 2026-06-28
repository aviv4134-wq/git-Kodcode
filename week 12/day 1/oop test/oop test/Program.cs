using System;

namespace Bank
{
    enum accountNames
    {
        Savings,
        Checking,
        Business
    }
    class BankAccount
    {
        private int _accountNumber;
        private string _ownerName;
        private double _balance;
        private string _accountType;
        private bool _isActive;
        private  List<string> _transactionHistory = new List<string>();
        public int AccountNumber 
        { get => _accountNumber; }
        
        public string OwnerName
        {
            get => _ownerName; 
            set 
            {
                if (string.IsNullOrWhiteSpace(value))
                    _ownerName = "Unknown";
                else
                    _ownerName = value;
            }    
        }

        public double Balance
        {
            get => _balance;
            set
            {
                if (value < 0)
                    _balance = 0;
                else 
                    _balance = value;
            }
        }

        public string AccountType
        {
            get => _accountType;
            set
            {
                if (Enum.TryParse<accountNames>(value, true, out accountNames _))
                    _accountType = value;
                else
                    _accountType = "Chcking";

            }
        }

        public bool IsActive
        {
            get => _isActive;
            set { _isActive = value; }
            
        }
        
        public BankAccount(int accountNumber, string ownerName, double balance, string accountType)
        {
            _accountNumber =  accountNumber;
            OwnerName = ownerName;
            Balance = balance;
            AccountType = accountType;
            IsActive = true;
        }

        public BankAccount(int accountNumber, string ownerName) : this(accountNumber, ownerName,0.0, "Checking")
        {

        }

        public BankAccount(int accountNumber, string ownerName, double initialDeposit) : this(accountNumber,  ownerName,  initialDeposit, "Checking")
        {

        }
        public override string ToString()
        
        => $"Account {AccountNumber} | Owner: {OwnerName} | Balance: ${Balance:F2} | Type: {AccountType} is active:{IsActive}";

        public void Deposit(double amount)
        {
            if (amount < 0)
                Console.WriteLine("error only positive number allowed");
            if (IsActive == false)
            {
                Console.WriteLine("error the account not active"); 
            }
            else
                Balance += amount;
                _transactionHistory.Add($"Deposit {amount}");
               Console.WriteLine("seccess to deposit");
        }

        public bool Withdraw(double amount)
        {
            if (amount < 0)
            {
                Console.WriteLine("error only positive number allowed");
                return false;
            }
            else if (Balance <= amount)
            {
                Console.WriteLine("error to withdraw the amount miust be bigger than the balance");
                return false;
            }
            if (IsActive == false)
            {
                Console.WriteLine("error the account not active");
                return false;
            }
            else
            {
                Console.WriteLine("seccess to withdraw");
                Balance -= amount;
                _transactionHistory.Add($"withdraw {amount}");
                return true;
            }
        }

        public void ApplyInterest()
        {
            if (AccountType == "Savings" || AccountType == "savings")
            {
                Balance *= 1.02;
            }
        }

        public void Activate()
        {
            IsActive = true;
        }

        public void Deactivate()
        {
            IsActive = false;
        }

        public void PrintTransactionHistory()
        {
            foreach (string tranaction in _transactionHistory)
                Console.WriteLine(tranaction);
        }

        public static bool Transfer(BankAccount from, BankAccount to, double amount)
        {
            if (!from.IsActive || !to.IsActive)
            {
                Console.WriteLine("one of the account not active");
                return false;
            }
            if (!from.Withdraw(amount))
                return false;

            to.Deposit(amount);
            from._transactionHistory.Add($"transfer to {to.OwnerName} {amount}");
            to._transactionHistory.Add($"recived from {from.OwnerName} {amount}");
            Console.WriteLine($"seccess to transfer to {to.OwnerName}");
            return true;
        } 




            static void Main()
            {
                BankAccount avi = new BankAccount(1, "avi");
                BankAccount bob = new BankAccount(2, "bob");
                BankAccount nadav = new BankAccount(3, "nadav", 300, "Savings");
                BankAccount hadas = new BankAccount(4, "hadas", 50);
                BankAccount guy = new BankAccount(5, "guy", 10, "Savings");
                BankAccount f1 = new BankAccount(6, "", -1, "Savinfgs");
                avi.Deposit(100);
                bob.Deposit(10);
                
                hadas.Withdraw(1032);
            Console.WriteLine(nadav);
            nadav.Deactivate();
            nadav.Withdraw(2);
            Console.WriteLine(nadav);
            List<BankAccount> accounts = [avi, bob, nadav, hadas, guy];


            }

    }      
 }