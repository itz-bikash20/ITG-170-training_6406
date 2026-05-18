public class Main{
    public static void main(String[] args){
        Employee em = new Employee(8);
        System.out.println(em.work());
        System.out.println(em.getSalary());
    }
}
class Employee{
    int hours;

    public Employee(int hours){
        this.hours = hours;
    }

    public int work(){
        return hours;
    }

    public int getSalary(){
        return hours * 1000;
    }
}