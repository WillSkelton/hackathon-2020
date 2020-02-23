package lib

type User struct {
	Name     string
	Email    string
	Password string
	UserID   int
}

var (
	id = 0
)

func NewUser(name, email, password string) (u *User, err error) {
	u = &User{}
	u.Name = name
	u.Email = email
	u.Password = password
	u.UserID = id

	if err == nil {
		id++
	}
	return
}
