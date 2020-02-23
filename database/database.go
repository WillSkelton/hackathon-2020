package database

import "hackathon-rest-server-2020/lib"

type DB struct {
	ID2Usr     map[int]*lib.User
	Email2User map[string]*lib.User
	NumUsers   int
}

func NewDB() (db *DB, err error) {
	db = &DB{}
	db.ID2Usr = make(map[int]*lib.User, 0)
	db.Email2User = make(map[string]*lib.User, 0)
	db.NumUsers = 0

	return
}

func (db *DB) PutUser(u *lib.User) (id int) {
	db.ID2Usr[u.UserID] = u
	db.Email2User[u.Email] = u

	return u.UserID
}
