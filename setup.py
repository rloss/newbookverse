import os

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, str):
            os.makedirs(base_path, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

project = {
    "bookverse": {
        ".gitignore": "node_modules\n.env\n__pycache__\n.next\n*.pyc\n",
        ".env.example": "DATABASE_URL=postgresql://user:pass@localhost:5432/app\nNEXT_PUBLIC_API_URL=http://localhost:8000",
        "README.md": "# Bookverse | 독서 모임 플랫폼",
        "docker-compose.yml": "version: '3.8'\nservices:\n  backend:\n    build: ./backend\n    ports:\n      - '8000:8000'\n  frontend:\n    build: ./frontend\n    ports:\n      - '3000:3000'",
        "render.yaml": "",

        "frontend": {
            ".env.production": "NEXT_PUBLIC_API_URL=https://bookverse-backend.onrender.com\nNODE_VERSION=18.17.1\nPORT=3000",
            "tailwind.config.ts": "// Tailwind config",
            "tsconfig.json": "{ \"compilerOptions\": { \"target\": \"esnext\" } }",
            "next.config.js": "module.exports = { reactStrictMode: true };",
            "public": {"logo.svg": ""},
            "styles": {"globals.css": "@tailwind base;\n@tailwind components;\n@tailwind utilities;"},
            "lib": {
                "api": {
                    "posts.ts": "",
                    "groups.ts": "",
                    "users.ts": "",
                    "books.ts": ""
                },
                "auth.ts": "",
                "utils.ts": ""
            },
            "components": {
                "layout": {},
                "post": {},
                "group": {},
                "book": {},
                "auth": {},
                "ui": {}
            },
            "app": {
                "layout.tsx": "export default function Layout({ children }) { return <>{children}</>; }",
                "page.tsx": "export default function Home() { return <main>메인</main>; }",
                "login": {"page.tsx": ""},
                "signup": {"page.tsx": ""},
                "my": {
                    "page.tsx": "",
                    "posts": {"page.tsx": ""},
                    "books": {"page.tsx": ""},
                    "groups": {"page.tsx": ""},
                    "stats": {"page.tsx": ""},
                    "settings": {"page.tsx": ""}
                },
                "groups": {
                    "page.tsx": "",
                    "[groupId]": {
                        "page.tsx": "",
                        "books": {"page.tsx": ""},
                        "posts": {"page.tsx": ""},
                        "community": {"page.tsx": ""},
                        "calendar": {"page.tsx": ""},
                        "my": {"page.tsx": ""},
                        "settings": {"page.tsx": ""},
                        "members": {"page.tsx": ""}
                    }
                },
                "books": {
                    "page.tsx": "",
                    "[bookId]": {"page.tsx": ""}
                },
                "write": {"page.tsx": ""},
                "error": {"not-found.tsx": ""}
            }
        },

        "backend": {
            ".env": "DATABASE_URL=sqlite:///./test.db",
            "requirements.txt": "fastapi\nsqlalchemy\npydantic\nuvicorn\nalembic",
            "test_main.py": "",
            "backend_boost.py": "",
            "app": {
                "__init__.py": "",
                "main.py": "# FastAPI main entry",
                "api": {
                    "__init__.py": "",
                    "deps.py": "",
                    "v1": {
                        "__init__.py": "",
                        "auth.py": "",
                        "users.py": "",
                        "groups.py": "",
                        "posts.py": "",
                        "books.py": "",
                        "groupbooks.py": "",
                        "comments.py": "",
                        "schedules.py": ""
                    }
                },
                "models": {
                    "__init__.py": "",
                    "base.py": "",
                    "user.py": "",
                    "group.py": "",
                    "group_user.py": "",
                    "book.py": "",
                    "group_book.py": "",
                    "post.py": "",
                    "comment.py": "",
                    "schedule.py": ""
                },
                "schemas": {
                    "__init__.py": "",
                    "user.py": "",
                    "auth.py": "",
                    "group.py": "",
                    "group_user.py": "",
                    "book.py": "",
                    "group_book.py": "",
                    "post.py": "",
                    "comment.py": "",
                    "schedule.py": ""
                },
                "services": {
                    "__init__.py": "",
                    "user_service.py": "",
                    "auth_service.py": "",
                    "group_service.py": "",
                    "post_service.py": "",
                    "comment_service.py": "",
                    "book_service.py": "",
                    "group_book_service.py": "",
                    "schedule_service.py": ""
                },
                "db": {
                    "session.py": "",
                    "init_db.py": "",
                    "base.py": ""
                },
                "core": {
                    "config.py": "",
                    "security.py": "",
                    "exceptions.py": "",
                    "logging.py": ""
                },
                "utils": {
                    "datetime.py": "",
                    "id_generator.py": "",
                    "enums.py": ""
                }
            },
            "alembic": {
                "env.py": "",
                "versions": {}
            },
            "tests": {
                "conftest.py": "",
                "test_users.py": "",
                "test_posts.py": "",
                "test_groups.py": "",
                "test_groupbooks.py": "",
                "test_auth.py": ""
            }
        }
    }
}

if __name__ == "__main__":
    create_structure(".", project)
    print("✅ Bookverse 디렉토리 구조 생성 완료!")
