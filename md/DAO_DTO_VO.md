# DAO (Data Access Object)

데이터베이스의 데이터에 접근하기 위해 생성하는 객체

비즈니스 로직과 DB 접근 로직을 분리하기 위해 사용하며 분리했을 때 재사용성이 증가한다.

> 해당 객체의 역할은 데이터 CRUD(Create, Read, Update, Delete) 작업을 실행하는 것이다.
Query를 통해서 DB 데이터를 조회 및 조작하는 메서드들을 가진 클래스를 DAO라고 부를 수 있다.
> 

```java
public class PersonDAO {
		public void addPerson(Person person){ ... }
		public List<Person> getAllPerson(){ ... }
		public Person getPerson(int id){ ... }
		public void removePerson(int id){ ... }
}
```

# DTO (Data Transfer Object)

비즈니스 로직을 담고있지않은 계층간 데이터 교환을 위한 객체

일반적으로 비즈니스 로직을 담고있지않아야하고 Getter와 Setter 둘 다 존재한다.

→ 위 내용은 DTO의 조건이 아니며 예외도 있다.

**특징**

- 비즈니스 로직과 데이터 구조 분리
    - 코드 관리가 편리해지고 깔끔하게 유지할 수 있다.
- 필요한 데이터만 전달하여 보안 강화
    - 필요한 데이터만 포함하여 다른 정보들에 대한 접근을 제한한다.
- 클라이언트와 서버간의 데이터 표준화
    - 규격이 바뀌어도 DB를 수정하지 않아도 된다.

> API 요청 규격 또는 응답 규격 Class를 DTO라고 부를 수 있다.
> 

```java
@Getter
@Setter
public class GetPersonResponse {
    private long    personId;
    private String  name;
    private String  email;
}
```

# VO (Value Object)

불변 클래스이며 값 자체를 비교할 수 있는 객체

- ****equals & hash code 메서드를 재정의****
    
    ```java
    ...
        @Override
        public boolean equals(final Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            final Point point = (Point) o;
            return x == point.x &&
                    y == point.y;
        }
    
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    ...
    ```
    
- ****수정자(setter)가 없는 불변 객체****

> Point나 Color를 떠올리면 조금 쉽게 다가온다.
x와 y 좌표로 이루어진 하나의 위치, RGB값이 각각 있는 색을 하나의 객체로 볼 수 있다.

원래 객체는 인스턴스화 하여 하나의 인스턴스를 만든 것을 의미한다. 
2개의 인스턴스를 비교하면 주소를 참조하기 때문에 값이 동일해도 동일한 객체로 인지하지 못한다.

동일한 색이지만 다른 값으로 인지하는 이 상황이 오히려 이상하게 느껴질 것이다. 위치도 동일하다.
이 때 VO의 필요성을 느낄 수 있다.
> 

```java
public class Point {
  private int x;
  private int y;

  public Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
```

- 참고
    
    https://tecoble.techcourse.co.kr/post/2020-06-11-value-object/
