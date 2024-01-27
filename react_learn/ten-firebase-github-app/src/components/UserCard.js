import React from "react";
import { Card,CardBody } from "reactstrap";

const UserCard = ({user}) => {
    return (
        <Card className="text-center mt-3 mb-4 align-items-center">
            <img src={user.avatar_url} alt="avatar" className="img-thumbnail w-50 h-50" />
            <CardBody>
                <div className="text-primary">{user.name}</div>
                <div className="text-primary">{user.location}</div>
                <div className="text-primary">{user.bio}</div>
                <div className="text-primary">Available for Hire: {user.hireable ? 'YES' : 'NOPE'}</div>
                <div className="text-primary">Followers: {user.followers}</div>
            </CardBody>
        </Card>
    )

}

export default UserCard