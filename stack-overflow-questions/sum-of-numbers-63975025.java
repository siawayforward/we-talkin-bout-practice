//Question from stackoverflow
//Source: https://stackoverflow.com/questions/63974941/how-to-get-a-formula-of-add-subtract-add-vice-versa-in-this-output/63975025#63975025


Scanner input = new Scanner(System.in);

    System.out.print("Enter value of n: ");
    nValue = input.nextInt(); 
    //variable for total value before loop
    int total = 0
    for (int x = 1; x <= nValue; x++){
        System.out.print("Enter number " + x + ": ");
        num = input.nextInt();
        //add or subtract to total with each iteration
        if(x%2==0){
            total += num;
        }            
        else {
            total -= num;
        }
    }
System.out.println("Answer: " + total);

//Excel python question answered
//https://stackoverflow.com/questions/63981188/search-for-keyboard-in-excel-and-extract-it-with-python/63981404