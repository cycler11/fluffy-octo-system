use actix_web::{web, App, HttpServer, Responder, HttpResponse};
use dotenvy::dotenv;
use std::env;

async fn index() -> impl Responder {
    HttpResponse::Ok().body("Магазин работает!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    dotenv().ok();
    let host = "0.0.0.0";
    let port = 8080;

    println!("Сервер запущен на http://{}:{}", host, port);

    HttpServer::new(|| {
        App::new()
            .route("/", web::get().to(index))
    })
    .bind((host, port))?
    .run()
    .await
}
