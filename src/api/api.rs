use actix_web::{web, get, post, delete, put, HttpResponse};
use crate::{models::task::Task, repository::database::Database};


#[post("/tasks")]
pub async fn create_task(db: web::Data<Database>, new_task: web::Json<Task>) -> HttpResponse {
    let task = db.create_task(new_task.into_inner());
    match task {
        Ok(task) => HttpResponse::Ok().json(task),
        Err(err) => HttpResponse::InternalServerError().body(err.to_string()),
    }
}

#[get("/tasks/{id}")]
pub async fn get_task_by_id(db: web::Data<Database>, id: web::Path<String>) -> HttpResponse {
    let task = db.get_task_by_id(&id);

    match task {
        Some(task) => HttpResponse::Ok().json(task),
        None => HttpResponse::NotFound().body("Task not found"),
    }
}

#[get("/tasks")]
pub async fn get_tasks(db: web::Data<Database>) -> HttpResponse {
    let tasks = db.get_tasks();
    HttpResponse::Ok().json(tasks)
}

#[delete("/tasks/{id}")]
pub async fn delete_task_by_id(db: web::Data<Database>, id: web::Path<String>) -> HttpResponse {
    let task = db.delete_task_by_id(&id);
    match task {
        Some(_) => HttpResponse::Ok().finish(),
        None => HttpResponse::NotFound().body("task not found"),
    }
}

#[put("/tasks/{id}")]
pub async fn update_task_by_id(db: web::Data<Database>, id: web::Path<String>, updated_task: web::Json<Task>) -> HttpResponse {
    let task = db.update_task_by_id(&id, updated_task.into_inner());
    match task {
        Some(task) => HttpResponse::Ok().json(task),
        None => HttpResponse::NotFound().body("Task not found"),
    }
}

pub fn config(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::scope("/api")
            .service(create_task)
            .service(get_task_by_id)
            .service(get_tasks)
            .service(delete_task_by_id)
            .service(update_task_by_id)
    );
}