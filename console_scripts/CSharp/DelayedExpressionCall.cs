List<int> numbers = new List<int>
{
    1,2,3,4,5,6,7,8,9,10
};

Debug.WriteLine("Before IEnumerable is declared");

var evenNumbers = numbers.Where((n) => {
    Debug.WriteLine(n);
    return n % 2 == 0;
});

Debug.WriteLine("After IEnumerable is declared");

evenNumbers.ToList();
