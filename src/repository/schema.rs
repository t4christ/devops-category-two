// @generated automatically by Diesel CLI.

diesel::table! {
    tasks (id) {
        #[max_length = 255]
        id -> Varchar,
        #[max_length = 255]
        title -> Varchar,
        description -> Nullable<Text>,
        created_at -> Nullable<Timestamp>,
        updated_at -> Nullable<Timestamp>,
    }
}
