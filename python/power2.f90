PROGRAM power
 INTEGER :: i, value
 CHARACTER(len=32) :: arg
 CALL getarg(1, arg)
 read (arg,'(I10)') value
 call power2(value)
END PROGRAM
!
subroutine power2(i)
implicit none
integer:: i,x,p
integer::products(10)
x = 1
do
   if(i<=0) exit
   p = mod(i,2)
    if(p > 0) then
      products(i)=x
      write(*,*) x
   end if
   x = x*2
   i = ishft(i,-1)
end do
end
