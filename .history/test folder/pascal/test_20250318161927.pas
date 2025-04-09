program SumOfNumbers;
var
  n, i, sum: integer;
begin
  sum := 0;
  write('Enter a number: ');
  readln(n);
  for i := 1 to n do
    sum := sum + i;
  writeln('Sum: ', sum);
end.
