from fastapi import FastAPI
from routes.route import router
from mangum import Mangum
from routes.manageClassesRoute import manageClassesRouter
from routes.teachingMaterialRoute import manageTeachingMaterialRouter
from routes.assignStudentWorkRoute import assignStudentWorkRouter

app = FastAPI()

app.include_router(router)
app.include_router(manageClassesRouter)
app.include_router(manageTeachingMaterialRouter)
app.include_router(assignStudentWorkRouter)

handler = Mangum(app)