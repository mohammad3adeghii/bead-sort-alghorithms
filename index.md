
<h2><b>A Implemention of bead-sort alghorithms</b></h2>
<hr>
<br>
<h4><b>Introduction</b></h4>
<hr>
<br>
<span>Bead-sort is a sorting alghorithms that can sort a list of positive integers.</span>
<span><br>For example:<br></span>
<span>porpus we have a array like [1, 5, 3, 2] this is a non sorted array so we can sorted this array with bead-sort alghorithms.</span>
<span><br> alright! the questions is has a bulited function with names sort or sorted in python with default will problems we can builted a sort function in python.</span>
<span><br> will we heres writes alghorithms:<br></span>
<span>
    def bead_sort(arr):
        if any(not isinstance(x, int) or x < 0 for x in arr):
            return TypeError("arr most be is integers")

        for _ in range(len(arr)):
            for i , (upper, lower) in enumerate(zip(arr, arr[1:]))
                if upper > lower:
                    arr[i] -= upper - lower
                    arr[i+1] += upper - lower

        return arr

    bead_sort([1, 5, 3, 2])
</span>
<span>
    <br>so output:<br>
</span>
<span>
    [1,2,3,5]
</span>

<span>
    <br> alright <br>
    <b>def bead_sort(arr)</b>
    <br>
    we this line the defination function with name bead_sort and given a one parameters (arr)
    <br>
    <b>
        if any(not isinstance(x, int) or x < 0 for x in arr):
            raise TypeError("arr most be is integers")
    </b>
    will, 
    any method is a itterable method this command when condintion is true is return a below blocks
    <br> if is not true returns a itterable
    <br>
    will, in the onouther lines we alternates the indexes item
</span>