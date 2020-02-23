package api

import (
	"encoding/json"
	"fmt"
	"hackathon-rest-server-2020/database"
	"hackathon-rest-server-2020/lib"
	"log"
	"net/http"
)

const (
	port         = "42201"
	tempHomePage = `<h1>YEET</h1>`
)

type ReqData struct {
	Name     string `json:"name"`
	Email    string `json:"email"`
	Password string `json:"password"`
	UserID   int
}

var (
	DB *database.DB
)

func newUser(w http.ResponseWriter, r *http.Request) {
	enableCors(&w)
	fmt.Println("Endpoint hit: /newuser")
	reqData := ReqData{}

	decoder := json.NewDecoder(r.Body)
	decoder.Decode(&reqData)

	u, _ := lib.NewUser(reqData.Name, reqData.Email, reqData.Password)

	fmt.Fprintf(w, "%v", DB.PutUser(u))

	fmt.Println("%v", DB)

}

func handleRequests() {
	http.HandleFunc("/newuser", newUser)

	fmt.Println("Listening on port: 42201")
	log.Fatal(http.ListenAndServe(":"+port, nil))
}

// Start will setup the routes and their respective functions as well as telling the
// server which port to listen on
func Start() {
	DB, _ = database.NewDB()
	handleRequests()
}

func enableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
}
