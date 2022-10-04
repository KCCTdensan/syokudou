import { Sequelize, DataTypes, Model } from "sequelize"

export class Activity extends Model {}
const ActivityAttr = {
  code: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  event: {
    type: DataTypes.STRING, // "used"
    allowNull: false,
  },
  date: {
    type: DataTypes.DATE,
    allowNull: false,
    defaultValue: DataTypes.NOW,
  },
}

export default async function init(path) {
  const sequelize = new Sequelize({
    dialect: "sqlite",
    storage: path,
  })

  Activity.init(ActivityAttr, { sequelize, timestamps: false })

  await Activity.sync()
}
