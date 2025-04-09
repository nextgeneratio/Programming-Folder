program PrimeCheck;
var
  num, i: integer;
  isPrime: boolean;
begin
  write('Enter a number: ');
  readln(num);
  isPrime := true;
  if num < 2 then
    isPrime := false;
  for i := 2 to num div 2 do
    if num mod i = 0 then
      isPrime := false;
  if isPrime then
    writeln('Prime')
  else
    writeln('Not Prime');
end.

